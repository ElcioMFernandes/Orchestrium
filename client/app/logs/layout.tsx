import type { ReactNode } from "react";

export default function LogsLayout({ children }: { children: ReactNode }) {
  return (
    <div className="flex-1 flex flex-col">
      <header className="border-b p-4">
        <h1 className="text-2xl font-bold">Logs</h1>
      </header>
      <div className="flex-1 p-4">{children}</div>
    </div>
  );
}
