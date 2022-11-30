<template>
  <q-page class="flex flex-center">

    <q-form>

      <div>
        <q-input style="margin-bottom:15px;" v-model="username" placeholder="Enter username" filled type="text" />
      </div>

      <div>
        <q-input style="margin-bottom:15px;" v-model="password" filled type="password" placeholder="Enter password" />
      </div>

      <div>
        <input enctype="multipart/form-data" type="file" name="file" id="">
      </div>

      <div  style="margin-top:15px;" class="flex flex-center">
        <q-btn color="primary" @click="upload" label="Upload" />
      </div>

    </q-form>

  </q-page>
</template>


<script>
import axios from 'axios';
import { ref } from 'vue'

export default {
  setup () {
    return {
      file: ref(null)
    }
  },
  methods: {
    async upload(e) {
      const res = await axios.post(
        "http://127.0.0.1:8000/upload_reel",
        {
          username: this.username,
          password: this.password,
          file: e.target.files[0]
        }
      )
      console.log(res)
    }
  }
}
</script>
