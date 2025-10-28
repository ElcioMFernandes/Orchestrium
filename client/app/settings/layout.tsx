import type { ReactNode } from "react";
import { SidebarTrigger } from "@/components/ui/sidebar";

export default function SettingsLayout({ children }: { children: ReactNode }) {
  return (
    <div className="flex-1 flex flex-col">
      <header className="flex flex-row items-center justify-between px-2">
        <div className="flex flex-row items-center gap-2">
          <SidebarTrigger />
          <h1 className="text-xl font-bold">Settings</h1>
        </div>
      </header>
      <div className="flex-1 p-4">{children}</div>
    </div>
  );
}
