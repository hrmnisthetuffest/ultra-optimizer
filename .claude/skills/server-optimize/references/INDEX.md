# server-optimize reference index

Load only what the component or step needs. Every file uses the 13-section format and ends with a sources section; unfetched claims are marked unverified.

## deployment (shared by all commands)

- [access-levels-and-authorization](deployment/access-levels-and-authorization.md): Define the six progressive access levels and the explicit authorization each requires, so nothing live happens without consent.
- [command-integration](deployment/command-integration.md): Explain how /race, /optimize, /ping-optimize and /server-optimize use one shared library without duplicating it or blurring responsibilities.
- [detection-rules](deployment/detection-rules.md): Explain how deployment targets are inferred from repository files and how to extend the rules.
- [intake-workflow](deployment/intake-workflow.md): Define the mandatory first step of /server-optimize: one consolidated intake that gathers every material configuration answer before any analysis.
- [runtime-adaptation](deployment/runtime-adaptation.md): Let a RACE-using application adapt its OWN parameters (worker counts, concurrency, memory budgets, cache allocation, batch sizes, database pool sizes, scheduling slots) to verified server capabilities, within developer-approved bounds.
- [validation-and-rollback](deployment/validation-and-rollback.md): Define how every server-side change is validated under representative load and rolled back when validation fails and rollback is safe and authorized.
- [workload-profiling](deployment/workload-profiling.md): Describe how to establish a baseline and profile representative workloads safely before changing anything.

## server-domains (load per component)

- [api-performance](server-domains/api-performance.md): Make endpoints fast and cheap: right-sized payloads, fewer round trips, safe caching and pagination.
- [background-processing](server-domains/background-processing.md): Move slow work off the request path and run scheduled work safely.
- [caching](server-domains/caching.md): Avoid repeated work by reusing results safely, with correct keys, freshness and invalidation.
- [concurrency](server-domains/concurrency.md): Use concurrency to hide I/O wait and use cores, without races, deadlocks or overload.
- [containers](server-domains/containers.md): Build small, fast, correct images and run containers within sensible resource limits.
- [cpu-execution](server-domains/cpu-execution.md): Find and reduce CPU-bound work in server code and match parallelism to the verified core count.
- [data-integrity](server-domains/data-integrity.md): Ensure optimizations never lose, duplicate or corrupt data.
- [databases](server-domains/databases.md): Find slow or wasteful queries and connection patterns and fix them without risking data.
- [deployment](server-domains/deployment.md): Understand how code reaches production so optimizations ship safely.
- [event-loops](server-domains/event-loops.md): Keep single-threaded or cooperative runtimes responsive by never blocking the loop.
- [infrastructure-costs](server-domains/infrastructure-costs.md): Reduce cost per unit of work where measurable, never by reducing correctness or safety.
- [kubernetes](server-domains/kubernetes.md): Right-size requests, limits, probes and scaling for workloads on Kubernetes without changing cluster-level settings.
- [load-balancing](server-domains/load-balancing.md): Distribute traffic evenly and fail over quickly.
- [memory-management](server-domains/memory-management.md): Keep memory use within the host or container limit, avoid leaks and reduce allocation churn without risking out-of-memory kills.
- [message-queues](server-domains/message-queues.md): Improve queue throughput and latency while keeping delivery guarantees.
- [networking](server-domains/networking.md): Make the server's own network handling efficient: connections, protocols, buffers and timeouts.
- [observability](server-domains/observability.md): Provide the measurements optimization needs, without adding hidden telemetry.
- [recovery](server-domains/recovery.md): Preserve recoverability while optimizing.
- [reliability](server-domains/reliability.md): Keep the service correct and available under failure while optimizing.
- [request-lifecycle](server-domains/request-lifecycle.md): Break one request into stages (accept, TLS, routing, auth, parse, handler, data access, serialize, send) so time can be attributed to a stage.
- [scalability](server-domains/scalability.md): Identify limits to scaling and remove software bottlenecks before adding hardware.
- [security](server-domains/security.md): Make sure performance work never weakens security.
- [server-architecture](server-domains/server-architecture.md): Understand how the backend is decomposed (monolith, services, serverless, workers) so optimization targets the real critical path.
- [serverless](server-domains/serverless.md): Reduce cold starts, per-invocation overhead and cost on function platforms.
- [storage](server-domains/storage.md): Reduce storage latency and wasted I/O for disks, object stores and shared filesystems.
- [thread-pools](server-domains/thread-pools.md): Choose pool sizes and queue policies that match the workload mix (CPU-bound versus blocking I/O).
