# ping-optimize reference index

Load only the files the scope needs. Every file uses the 13-section format and has a sources section with access dates; unfetched claims are marked unverified.

## network-application-profiles

- [api-and-saas-networking](network-application-profiles/api-and-saas-networking.md): Fewer, cheaper, safer API calls.
- [browsers-networking](network-application-profiles/browsers-networking.md): Faster page and resource delivery for web apps, and understanding the network stack of browser-engine projects.
- [cloud-sync](network-application-profiles/cloud-sync.md): Efficient incremental synchronization and transfer scheduling.
- [downloads-and-uploads](network-application-profiles/downloads-and-uploads.md): Faster, resumable, verified transfers.
- [games-networking](network-application-profiles/games-networking.md): Lower perceived lag and improve consistency without altering gameplay rules or fairness.
- [messaging-networking](network-application-profiles/messaging-networking.md): Fast, reliable, deduplicated message delivery with robust reconnection and offline sync.
- [video-streaming](network-application-profiles/video-streaming.md): Faster start, fewer rebuffers, stable quality without breaking sync.

## network-benchmarks

- [application-network-profiling](network-benchmarks/application-network-profiling.md): Profile the app's actual requests and attribute time.
- [bandwidth-benchmarks](network-benchmarks/bandwidth-benchmarks.md): Measure goodput honestly and cheaply.
- [jitter-and-packet-loss](network-benchmarks/jitter-and-packet-loss.md): Measure variation and loss for real-time paths.
- [latency-benchmarks](network-benchmarks/latency-benchmarks.md): Measure RTT and operation latency as distributions.
- [loaded-latency](network-benchmarks/loaded-latency.md): Measure how latency grows when the link is busy with the app's own traffic.
- [network-regression-testing](network-benchmarks/network-regression-testing.md): Keep network behavior from regressing after changes.

## network-intelligence

- [bandwidth-analysis](network-intelligence/bandwidth-analysis.md): Separate 'the link is slow' from 'the app uses the link badly'. Throughput is bits delivered per second; it says little about latency.
- [congestion-analysis](network-intelligence/congestion-analysis.md): Congestion shows up as growing queueing delay and loss under load. The application must avoid causing or worsening it.
- [connection-management](network-intelligence/connection-management.md): Most avoidable latency comes from opening connections too often or using stale ones.
- [dns-intelligence](network-intelligence/dns-intelligence.md): DNS lookup precedes the first connection to a host. The application can reduce lookups and avoid blocking on them; it cannot change the user's resolver.
- [http-protocols](network-intelligence/http-protocols.md): HTTP/1.1, HTTP/2 and HTTP/3 offer different tradeoffs. Detect what the client, server and path actually negotiate; never assume newer is faster for a given workload.
- [http2](network-intelligence/http2.md): HTTP/2 multiplexes many request/response streams over one TCP connection, with header compression and flow control.
- [http3-and-quic](network-intelligence/http3-and-quic.md): HTTP/3 maps HTTP onto QUIC, which runs over UDP with per-stream loss recovery and integrated TLS 1.3.
- [jitter-analysis](network-intelligence/jitter-analysis.md): Jitter is variation in delay. Real-time audio, video and games care about it more than about mean latency.
- [latency-analysis](network-intelligence/latency-analysis.md): Attribute user-perceived delay to its cause before changing anything. Latency has nine places to hide: (1) application logic, (2) local networking implementation (queues, thread pools, serialization), (3) DNS, (4) connection establishment (TCP, TLS, QUIC), (5) transport behavior (slow start, loss recovery, head-of-line blocking), (6) network path, (7) remote server processing, (8) data transfer, (9) client processing after the response arrives.
- [network-detection](network-intelligence/network-detection.md): Decide what the application can legitimately learn about its connection and how to use it. The application may read what supported APIs expose (for example the browser Network Information API where available, platform reachability callbacks, its own request timings). It must not change any device or network setting.
- [packet-loss-analysis](network-intelligence/packet-loss-analysis.md): Loss changes the right strategy. Reliable transports hide loss as delay; unreliable ones expose it as missing data.
- [ping-analysis](network-intelligence/ping-analysis.md): Explain what a 'ping' is and is not. ICMP echo RTT, TCP connect time, application-level request RTT and server response time are different quantities. The application can lower round-trip COUNT and connection setup COST; it cannot lower physical path delay.
- [server-response-analysis](network-intelligence/server-response-analysis.md): Separate time spent waiting for the server from time spent in the network. Only the server owner can fix the former, and RTT cannot be inferred from it.
- [tcp-intelligence](network-intelligence/tcp-intelligence.md): TCP gives reliable ordered delivery at the cost of handshake latency and head-of-line blocking. The app influences it through connection reuse, buffer use and write patterns, not OS tuning.
- [tls-intelligence](network-intelligence/tls-intelligence.md): TLS adds handshake round trips and CPU work. Improve performance by reusing sessions and connections, never by weakening verification or ciphers.

## network-optimization

- [adaptive-bandwidth](network-optimization/adaptive-bandwidth.md): Let the application adjust its OWN networking behavior to measured conditions, with evidence and limits. This is the RACE-style adaptive layer for networking.
- [caching](network-optimization/caching.md): Avoid transfers by reusing valid data, while preserving freshness and confidentiality.
- [compression](network-optimization/compression.md): Smaller payloads transfer faster when bandwidth or loss is the limit. Compression costs CPU and can leak secrets in some attack settings.
- [concurrency](network-optimization/concurrency.md): Right-size parallelism. More parallelism helps latency-bound independent work and hurts under bandwidth limits, loss, rate limits or shared bottlenecks.
- [connection-pooling](network-optimization/connection-pooling.md): Reuse connections to avoid repeated DNS, TCP and TLS cost.
- [latency-reduction](network-optimization/latency-reduction.md): Ordered checklist for lowering user-perceived waiting.
- [prefetching](network-optimization/prefetching.md): Fetching early can hide latency but wastes data and can slow critical work. Prefetch only when the need is probable and the cost bounded.
- [request-optimization](network-optimization/request-optimization.md): Reduce the number, size and waiting of requests without changing what the user gets.
- [retry-and-recovery](network-optimization/retry-and-recovery.md): Retries recover transient failure but can create duplicates and storms. Design them deliberately.
- [streaming](network-optimization/streaming.md): Stream when partial data is useful early; chunk when resumption or memory limits matter.
