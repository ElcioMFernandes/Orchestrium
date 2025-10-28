import useSWR from "swr";
import fetcher from "@/lib/fetcher";
import { TypeTask } from "@/types/task";

const useTasksGetter = () => {
  const { data, isLoading, error } = useSWR<TypeTask[]>(`tasks`, fetcher);

  return { data, isLoading, error };
};

export default useTasksGetter;
