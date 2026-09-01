import httpx
from pathlib import Path
from PIL import Image
import io

Path("data/radar").mkdir(parents=True, exist_ok=True)

urls = [
    "https://mausam.imd.gov.in/Radar/caz_hyd.gif",
    "https://mausam.imd.gov.in/Radar/dist_hyd.gif",
    "https://mausam.imd.gov.in/Radar/ppz_hyd.gif",
    "https://mausam.imd.gov.in/Radar/max_hyd.gif",
    "https://mausam.imd.gov.in/Radar/animation/Converted/HYD_MAXZ.gif",
    "https://mausam.imd.gov.in/Radar/animation/Converted/HYD_SRI.gif",
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "Referer": "https://mausam.imd.gov.in/",
}

print("Querying IMD Doppler Weather Radar endpoints for Hyderabad...")
with httpx.Client(headers=headers, timeout=20.0, verify=False) as client:
    for url in urls:
        filename = url.split("/")[-1]
        try:
            r = client.get(url)
            ct = r.headers.get("content-type", "unknown")
            print(f"{url} -> status={r.status_code}, bytes={len(r.content)}, type={ct}")
            if r.status_code == 200 and len(r.content) > 1000:
                save_path = Path("data/radar") / filename
                with open(save_path, "wb") as f:
                    f.write(r.content)
                print(f"  [SAVED] {save_path}")
                try:
                    img = Image.open(io.BytesIO(r.content))
                    print(f"  [IMAGE INFO] format={img.format}, size={img.size}, mode={img.mode}, animated={getattr(img, 'is_animated', False)}")
                except Exception as img_err:
                    print(f"  [IMAGE ERR] {img_err}")
        except Exception as e:
            print(f"{url} -> error: {e}")
