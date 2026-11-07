<#
 Removes only files recorded in the installer manifest whose hash still matches.
 STATUS: written but NOT tested (no PowerShell available in the build environment).
#>
param([ValidateSet('project','personal')][string]$Scope = 'project', [string]$Target = '', [switch]$DryRun)
$ErrorActionPreference = 'Stop'
if (-not $Target) {
  if ($Scope -eq 'personal') { $Target = Join-Path $env:USERPROFILE '.claude\skills' }
  else { $Target = Join-Path (Get-Location) '.claude\skills' }
}
$manifest = Join-Path $Target '.ultra-optimizer-manifest.tsv'
if (-not (Test-Path $manifest)) { Write-Host "No installer manifest at $manifest; nothing removed."; return }
$removed = 0; $kept = @()
foreach ($line in Get-Content $manifest) {
  $parts = $line -split "`t", 2
  if ($parts.Count -lt 2) { continue }
  $p = Join-Path $Target ($parts[1] -replace '/','\')
  if (-not (Test-Path $p)) { continue }
  if ((Get-FileHash $p).Hash.ToLower() -eq $parts[0]) { if ($DryRun) { Write-Host "[dry-run] remove $($parts[1])" } else { Remove-Item $p -Force }; $removed++ }
  else { $kept += $parts[1] }
}
if (-not $DryRun) {
  foreach ($n in 'race','optimize') {
    $d = Join-Path $Target $n
    if (Test-Path $d) { Get-ChildItem $d -Recurse -Directory | Sort-Object FullName -Descending | Where-Object { -not (Get-ChildItem $_.FullName -Force) } | Remove-Item; if (-not (Get-ChildItem $d -Force)) { Remove-Item $d } }
  }
  if ($kept.Count -eq 0) { Remove-Item $manifest -Force }
}
Write-Host "Removed files: $removed"
Write-Host "Kept (modified since install): $($kept -join ', ')"
