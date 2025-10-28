"use client";

import Link from "next/link";
import useTasks from "@/hooks/useTasksGetter";
import { Button } from "@/components/ui/button";

export default function Tasks() {
  const { data, isLoading, error } = useTasks();

  if (error) return <div>Error: {error.message}</div>;

  if (!data || isLoading) return <div>Loading...</div>;

  return (
    <div className="flex-1">
      <nav>
        <Button>
          <Link href={"/tasks/include"}>Add</Link>
        </Button>
      </nav>
      <ul>
        {data.length > 0 ? (
          data.map((task) => (
            <li key={task.id}>
              <Link href={`/tasks/${task.id}`}>{task.name}</Link>
            </li>
          ))
        ) : (
          <li>No tasks found.</li>
        )}
      </ul>
    </div>
  );
}
