import { useEffect, useState } from "react";

export function ClipList({ route }: { route?: string }) {
  const [clips, setClips] = useState<string[]>([]);
  useEffect(() => {
    fetch(`/api/clips?route=${route ?? ""}`).then(r => r.json()).then(setClips);
  }, [route]);
  return <ul>{clips.map(c => <li key={c}>{c}</li>)}</ul>;
}
// Paging: pass page=N to the API (was always sending page=1).
