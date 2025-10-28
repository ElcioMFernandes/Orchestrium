import useSWR from "swr";
import fetcher from "@/lib/fetcher";

const useTriggerGetter = (id: string) => {
  const { data, isLoading, error } = useSWR(`triggers/${id}`, fetcher);

  return { data, isLoading, error };
};

export default useTriggerGetter;
