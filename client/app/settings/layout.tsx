import type { ReactNode } from "react";

export default function SettingsLayout({ children }: { children: ReactNode }) {
  return (
    <div className="flex-1 flex flex-col">
      <header className="border-b p-4">
        <h1 className="text-2xl font-bold">Settings</h1>
      </header>
      <div className="flex-1 p-4">{children}</div>
    </div>
  );
}
