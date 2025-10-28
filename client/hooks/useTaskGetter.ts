import useSWR from "swr";
import fetcher from "@/lib/fetcher";

const useTaskGetter = (id: string) => {
  const { data, isLoading, error } = useSWR(`tasks/${id}`, fetcher);

  return { data, isLoading, error };
};

export default useTaskGetter;
