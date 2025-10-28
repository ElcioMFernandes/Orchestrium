import useSWR from "swr";
import fetcher from "@/lib/fetcher";

const useLogsGetter = () => {
  const { data, isLoading, error } = useSWR(`logs`, fetcher);

  return { data, isLoading, error };
};

export default useLogsGetter;
