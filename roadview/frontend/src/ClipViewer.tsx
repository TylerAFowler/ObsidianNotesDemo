export function ClipViewer({ src, recordedAt }: { src: string; recordedAt: string }) {
  return (
    <figure>
      <video src={src} controls width={960} />
      <figcaption>{new Date(recordedAt).toLocaleString()}</figcaption>
    </figure>
  );
}
