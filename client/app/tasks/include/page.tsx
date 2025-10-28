"use client";
import React from "react";

import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";

export default function IncludeTask() {
  const [name, setName] = React.useState("");
  const [content, setContent] = React.useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Submit the task to the server
    console.log({ name, content });
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="flex flex-col justify-between gap-4"
    >
      <fieldset className="flex-1 flex flex-col gap-4">
        <div className="flex flex-col gap-2">
          <Label htmlFor="name">Name</Label>
          <Input
            id="name"
            type="text"
            value={name}
            placeholder="Task name"
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div className="flex flex-col gap-2">
          <Label htmlFor="content">Content</Label>
          <Textarea
            id="content"
            value={content}
            placeholder="Type your code here."
            onChange={(e) => setContent(e.target.value)}
          />
        </div>
      </fieldset>
      <Button type="submit" disabled={!name || !content}>
        Submit
      </Button>
    </form>
  );
}
