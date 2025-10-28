import useSWR from "swr";
import fetcher from "@/lib/fetcher";

const useLogGetter = (id: string) => {
  const { data, isLoading, error } = useSWR(`logs/${id}`, fetcher);

  return { data, isLoading, error };
};

export default useLogGetter;
