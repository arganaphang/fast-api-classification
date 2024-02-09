<script lang="ts">
  import Form from "@/components/Form.svelte";
  import Table from "@/components/Table.svelte";
  import { add, get, reset } from "@/helper/local_database";
  import type { PredictRequest, PredictResponse } from "@/types/predict";
  import axios from "axios";

  let data = get();

  function onAdd(req: PredictRequest) {
    axios
      .post<PredictResponse>(
        `${import.meta.env.PUBLIC_BASE_API_URL}/predict`,
        req
      )
      .then((response) => {
        if (response.status === 200) {
          add({ ...req, response: response.data.message });
          data = get();
        }
      })
      .catch((err) => console.log(err));
  }

  function onReset() {
    reset();
    data = get();
  }
</script>

<div class="flex flex-col lg:flex-row px-12 py-8 gap-4">
  <Form {onAdd} />
  <Table {data} {onReset} />
</div>
