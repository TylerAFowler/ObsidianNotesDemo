import L from "leaflet";
import { useEffect, useRef } from "react";

export function MapView({ points }: { points: { lat: number; lon: number; id: string }[] }) {
  const el = useRef<HTMLDivElement>(null);
  useEffect(() => {
    const map = L.map(el.current!).setView([38.6, -80.6], 7);
    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(map);
    points.forEach(p => L.marker([p.lat, p.lon]).addTo(map));
    return () => { map.remove(); };
  }, [points]);
  return <div ref={el} style={{ height: 480 }} />;
}
// Clicking a cluster calls onSelect(ids) so ClipList can filter to those clips.
