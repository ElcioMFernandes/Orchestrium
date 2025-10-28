import useSWR from "swr";
import fetcher from "@/lib/fetcher";

const useJobsGetter = () => {
  const { data, isLoading, error } = useSWR(`jobs`, fetcher);

  return { data, isLoading, error };
};

export default useJobsGetter;
