import type { ReactNode } from "react";
import { TbChevronLeft } from "react-icons/tb";
import { Button } from "@/components/ui/button";

export default function IncludeJobLayout({
  children,
}: {
  children: ReactNode;
}) {
  return (
    <div className="flex-1 flex flex-col gap-2">
      <header className="flex flex-row items-center justify-between">
        <div className="flex flex-row items-center gap-2">
          <Button variant={"ghost"}>
            <TbChevronLeft />
          </Button>
          <h1 className="text-lg">Include Job</h1>
        </div>
      </header>
      <div className="flex-1">{children}</div>
    </div>
  );
}
