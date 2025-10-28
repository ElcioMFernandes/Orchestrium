import Link from "next/link";
import { Button } from "@/components/ui/button";

export default function Triggers() {
  return (
    <div className="flex-1">
      <nav>
        <Button>
          <Link href={"/triggers/include"}>Add</Link>
        </Button>
      </nav>
    </div>
  );
}
