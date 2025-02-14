import React, { useRef, useEffect, useState } from "react";

const VideoCall: React.FC = () => {
  const localVideoRef = useRef<HTMLVideoElement>(null);
  const remoteVideoRef = useRef<HTMLVideoElement>(null);
  const [stream, setStream] = useState<MediaStream | null>(null);

  useEffect(() => {
    navigator.mediaDevices.getUserMedia({ video: true, audio: true }).then((mediaStream) => {
      setStream(mediaStream);
      if (localVideoRef.current) localVideoRef.current.srcObject = mediaStream;
    });
  }, []);

  return (
    <div className="flex gap-4 p-4">
      <video ref={localVideoRef} autoPlay className="w-1/2 border rounded" />
      <video ref={remoteVideoRef} autoPlay className="w-1/2 border rounded" />
    </div>
  );
};

export default VideoCall;
