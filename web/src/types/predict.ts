export type PredictRequest = {
  nilai: number;
  homepage: boolean;
  modul_perkuliahan: boolean;
  forum: boolean;
  tugas: boolean;
  kuis: boolean;
  uts: boolean;
  uas: boolean;
};
export type PredictResponse = {
  message: string;
};

export type Predict = {
  nilai: number;
  homepage: boolean;
  modul_perkuliahan: boolean;
  forum: boolean;
  tugas: boolean;
  kuis: boolean;
  uts: boolean;
  uas: boolean;
  response: string;
};
