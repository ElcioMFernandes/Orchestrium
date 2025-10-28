export type TypeCreateTask = {
  name: string;
  content: string;
};

export type TypeTask = TypeCreateTask & {
  id: string;
};
