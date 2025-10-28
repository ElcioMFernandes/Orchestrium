import useSWR from "swr";
import fetcher from "@/lib/fetcher";

const useJobGetter = (id: string) => {
  const { data, isLoading, error } = useSWR(`jobs/${id}`, fetcher);

  return { data, isLoading, error };
};

export default useJobGetter;
