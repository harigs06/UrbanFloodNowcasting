type InundationCallback = (data: any) => void;

class WebSocketClient {
  private ws: WebSocket | null = null;
  private url: string;
  private callbacks: Set<InundationCallback> = new Set();
  private reconnectIntervalMs = 5000;
  private isExplicitlyClosed = false;
  private isConnected = false;

  constructor(url?: string) {
    const defaultWsUrl = `${window.location.protocol === 'https:' ? 'wss:' : 'ws:'}//${window.location.hostname}:8000/ws/inundation`;
    this.url = url || (import.meta.env.VITE_WS_URL || defaultWsUrl);
  }

  public connect(): void {
    this.isExplicitlyClosed = false;
    try {
      this.ws = new WebSocket(this.url);

      this.ws.onopen = () => {
        this.isConnected = true;
        console.log('[WebSocket] Connected to real-time inundation stream at', this.url);
      };

      this.ws.onmessage = (event) => {
        try {
          const payload = JSON.parse(event.data);
          this.callbacks.forEach(cb => cb(payload));
        } catch (e) {
          console.warn('[WebSocket] Error parsing JSON payload', e);
        }
      };

      this.ws.onerror = (err) => {
        console.debug('[WebSocket] Connection error (expected if backend offline)', err);
      };

      this.ws.onclose = () => {
        this.isConnected = false;
        if (!this.isExplicitlyClosed) {
          setTimeout(() => this.connect(), this.reconnectIntervalMs);
        }
      };
    } catch {
      this.isConnected = false;
      if (!this.isExplicitlyClosed) {
        setTimeout(() => this.connect(), this.reconnectIntervalMs);
      }
    }
  }

  public subscribe(cb: InundationCallback): () => void {
    this.callbacks.add(cb);
    if (!this.ws || this.ws.readyState === WebSocket.CLOSED) {
      this.connect();
    }
    return () => {
      this.callbacks.delete(cb);
    };
  }

  public getStatus(): boolean {
    return this.isConnected && this.ws?.readyState === WebSocket.OPEN;
  }

  public disconnect(): void {
    this.isExplicitlyClosed = true;
    if (this.ws) {
      this.ws.close();
    }
  }
}

export const inundationWs = new WebSocketClient();
