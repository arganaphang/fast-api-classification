<script lang="ts">
  import type { Predict } from "@/types/predict";
  export let data: Predict[];
  export let onReset: () => void;
</script>

<div class="flex flex-col">
  <div class="relative overflow-x-auto flex flex-col">
    <table class="w-full text-sm text-left rtl:text-right text-gray-500">
      <thead class="text-xs text-gray-700 uppercase bg-gray-50">
        <tr>
          <th scope="col" class="px-6 py-3"> # No </th>
          <th scope="col" class="px-6 py-3"> Nilai </th>
          <th scope="col" class="px-6 py-3"> Homepage </th>
          <th scope="col" class="px-6 py-3"> Modul Perkuliahan </th>
          <th scope="col" class="px-6 py-3"> Forum </th>
          <th scope="col" class="px-6 py-3"> Tugas </th>
          <th scope="col" class="px-6 py-3"> Kuis </th>
          <th scope="col" class="px-6 py-3"> UTS </th>
          <th scope="col" class="px-6 py-3"> UAS </th>
          <th scope="col" class="px-6 py-3"> Result </th>
        </tr>
      </thead>
      <tbody>
        {#each data as item, i}
          <tr class="bg-white border-b">
            <td class="px-6 py-4"> {i + 1} </td>
            <td class="px-6 py-4 text-center"> {item.nilai} </td>
            <td class="px-6 py-4 text-center">
              {item.homepage ? "✅" : "❌"}
            </td>
            <td class="px-6 py-4 text-center">
              {item.modul_perkuliahan ? "✅" : "❌"}
            </td>
            <td class="px-6 py-4 text-center"> {item.forum ? "✅" : "❌"} </td>
            <td class="px-6 py-4 text-center"> {item.tugas ? "✅" : "❌"} </td>
            <td class="px-6 py-4 text-center"> {item.kuis ? "✅" : "❌"} </td>
            <td class="px-6 py-4 text-center"> {item.uts ? "✅" : "❌"} </td>
            <td class="px-6 py-4 text-center"> {item.uas ? "✅" : "❌"} </td>
            <td class="px-6 py-4 text-center">
              <span
                class={`rounded-full px-4 py-2 text-xs text-nowrap text-${
                  item.response === "Bagus" ? "green" : "red"
                }-50 bg-${item.response === "Bagus" ? "green" : "red"}-400`}
                >{item.response}</span
              >
            </td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>

  <button
    class="self-end mt-8 px-12 py-3 rounded-md bg-dark text-light text-sm"
    on:click={onReset}
  >
    Reset
  </button>
</div>
