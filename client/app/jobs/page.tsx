import Link from "next/link";
import { Button } from "@/components/ui/button";

export default function Jobs() {
  return (
    <div className="flex-1">
      <nav>
        <Button>
          <Link href={"/jobs/include"}>Add</Link>
        </Button>
      </nav>
    </div>
  );
}
