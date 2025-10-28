import useSWR from "swr";
import fetcher from "@/lib/fetcher";

const useTriggersGetter = () => {
  const { data, isLoading, error } = useSWR(`triggers`, fetcher);

  return { data, isLoading, error };
};

export default useTriggersGetter;
