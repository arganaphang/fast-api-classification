<script lang="ts">
  import type { PredictRequest } from "@/types/predict";
  let data: PredictRequest = {
    nilai: 0,
    homepage: false,
    modul_perkuliahan: false,
    forum: false,
    tugas: false,
    kuis: false,
    uts: false,
    uas: false,
  };
  export let onAdd: (request: PredictRequest) => void;

  function handleSubmit(e: SubmitEvent) {
    onAdd({ ...data });
    data = {
      nilai: 0,
      homepage: false,
      modul_perkuliahan: false,
      forum: false,
      tugas: false,
      kuis: false,
      uts: false,
      uas: false,
    };
  }
</script>

<form
  class="w-full lg:w-[500px] flex flex-col gap-4"
  on:submit|preventDefault={handleSubmit}
>
  <label class="flex flex-col gap-2">
    <span class="text-sm text-slate-400">Nilai*</span>
    <input
      type="number"
      bind:value={data.nilai}
      min="0"
      max="100"
      class="rounded-md border-none"
    />
  </label>
  <label class="flex gap-2 items-center">
    <input
      type="checkbox"
      bind:checked={data.homepage}
      name="homepage"
      class="rounded-md"
    />
    <span class="text-sm text-slate-400">Homepage*</span>
  </label>
  <label class="flex gap-2 items-center">
    <input
      type="checkbox"
      bind:checked={data.modul_perkuliahan}
      name="modul_perkuliahan"
      class="rounded-md"
    />
    <span class="text-sm text-slate-400">Modul Perkuliahan*</span>
  </label>
  <label class="flex gap-2 items-center">
    <input
      type="checkbox"
      bind:checked={data.forum}
      name="forum"
      class="rounded-md"
    />
    <span class="text-sm text-slate-400">Forum*</span>
  </label>
  <label class="flex gap-2 items-center">
    <input
      type="checkbox"
      bind:checked={data.tugas}
      name="tugas"
      class="rounded-md"
    />
    <span class="text-sm text-slate-400">Tugas*</span>
  </label>
  <label class="flex gap-2 items-center">
    <input
      type="checkbox"
      bind:checked={data.kuis}
      name="kuis"
      class="rounded-md"
    />
    <span class="text-sm text-slate-400">Kuis*</span>
  </label>
  <label class="flex gap-2 items-center">
    <input
      type="checkbox"
      bind:checked={data.uts}
      name="uts"
      class="rounded-md"
    />
    <span class="text-sm text-slate-400">UTS*</span>
  </label>
  <label class="flex gap-2 items-center">
    <input
      type="checkbox"
      bind:checked={data.uas}
      name="uas"
      class="rounded-md"
    />
    <span class="text-sm text-slate-400">UAS*</span>
  </label>
  <button
    type="submit"
    class="px-12 py-3 rounded-md bg-dark text-light text-sm"
  >
    Submit
  </button>
</form>
