<#
 Ultra Optimizer installer for Windows PowerShell 5.1+ / PowerShell 7.
 STATUS: written but NOT tested (no PowerShell available in the build environment).
 Parameters mirror install.sh: -Scope project|personal, -Target, -Only, -Yes, -DryRun, -ForceBackup.
#>
param(
  [ValidateSet('project','personal')][string]$Scope = 'project',
  [string]$Target = '',
  [ValidateSet('','race','optimize','ping-optimize','server-optimize')][string]$Only = '',
  [switch]$Yes, [switch]$DryRun, [switch]$ForceBackup
)
$ErrorActionPreference = 'Stop'
$src = Join-Path (Split-Path -Parent $PSScriptRoot) '.claude\skills'
if (-not (Test-Path (Join-Path $src 'race')) -or -not (Test-Path (Join-Path $src 'optimize'))) { throw "source skills not found at $src" }
if (-not $Target) {
  if ($Scope -eq 'personal') { $Target = Join-Path $env:USERPROFILE '.claude\skills' }
  else { $Target = Join-Path (Get-Location) '.claude\skills' }
}
$names = if ($Only) { @($Only) } else { @('race','optimize','ping-optimize','server-optimize') }
$manifest = Join-Path $Target '.ultra-optimizer-manifest.tsv'
$ts = Get-Date -Format 'yyyyMMdd-HHmmss'
$bk = Join-Path $Target ".ultra-optimizer-backups\$ts"
function Get-Rel($root, $file) { $file.FullName.Substring($root.Length).TrimStart('\','/') }
function Same-Tree($a, $b) {
  if (-not (Test-Path $b)) { return $false }
  $fa = Get-ChildItem $a -Recurse -File | Where-Object { $_.Extension -ne '.pyc' -and $_.FullName -notmatch '__pycache__' }
  $fb = Get-ChildItem $b -Recurse -File | Where-Object { $_.Extension -ne '.pyc' -and $_.FullName -notmatch '__pycache__' }
  $ra = $fa | ForEach-Object { Get-Rel $a $_ } | Sort-Object
  $rb = $fb | ForEach-Object { Get-Rel $b $_ } | Sort-Object
  if (($ra -join "`n") -ne ($rb -join "`n")) { return $false }
  foreach ($r in $ra) { if ((Get-FileHash (Join-Path $a $r)).Hash -ne (Get-FileHash (Join-Path $b $r)).Hash) { return $false } }
  return $true
}
$installed = @(); $skipped = @(); $backed = @()
foreach ($n in $names) {
  $s = Join-Path $src $n; $d = Join-Path $Target $n
  if (Test-Path $d) {
    if (-not $ForceBackup -and (Same-Tree $s $d)) { $skipped += "$n (already up to date)"; continue }
    if (-not $Yes) {
      if ($DryRun) { Write-Host "[dry-run] would need -Yes to replace $d"; $skipped += "$n (needs -Yes)"; continue }
      $ans = Read-Host "Existing '$n' found at $d. Back it up and replace? [y/N]"
      if ($ans -notmatch '^(y|yes)$') { $skipped += "$n (existing kept)"; continue }
    }
    if ($DryRun) { Write-Host "[dry-run] backup $d -> $bk\$n" }
    else { New-Item -ItemType Directory -Force -Path $bk | Out-Null; Copy-Item $d (Join-Path $bk $n) -Recurse; Remove-Item $d -Recurse }
    $backed += "$d -> $bk\$n"
  }
  if ($DryRun) { Write-Host "[dry-run] install $s -> $d" }
  else {
    New-Item -ItemType Directory -Force -Path $Target | Out-Null
    Copy-Item $s $d -Recurse
    Get-ChildItem $d -Recurse -Force | Where-Object { $_.Name -eq '__pycache__' -or $_.Extension -eq '.pyc' } | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
  }
  $installed += $n
}
if (-not $DryRun -and $installed.Count -gt 0) {
  $lines = @()
  if (Test-Path $manifest) { $lines = Get-Content $manifest | Where-Object { $l = $_; -not ($installed | Where-Object { $l -like "*`t$_/*" }) } }
  foreach ($n in $installed) {
    $root = $Target.TrimEnd('\','/') + '\'
    Get-ChildItem (Join-Path $Target $n) -Recurse -File | Sort-Object FullName | ForEach-Object {
      $rel = (Get-Rel $root $_) -replace '\\','/'
      $lines += ((Get-FileHash $_.FullName).Hash.ToLower() + "`t" + $rel)
    }
  }
  Set-Content -Path $manifest -Value $lines
}
Write-Host "Target: $Target"
Write-Host "Installed: $($installed -join ', ')"
Write-Host "Skipped: $($skipped -join ', ')"
Write-Host "Backed up: $($backed -join ', ')"
