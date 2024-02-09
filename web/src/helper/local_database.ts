import type { Predict } from "@/types/predict";

const storage = localStorage;
const KEY = "responses";

export function add(predict: Predict) {
  const data = JSON.parse(storage.getItem(KEY) || "[]") as Predict[];
  return storage.setItem(KEY, JSON.stringify([...data, predict]));
}

export function get() {
  const data = JSON.parse(storage.getItem(KEY) || "[]") as Predict[];
  return data;
}

export function reset() {
  return storage.removeItem(KEY);
}
