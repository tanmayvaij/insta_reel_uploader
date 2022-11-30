<template>
  <q-page class="flex flex-center">
    <div>

      <q-uploader
        accept="video/mp4,video/x-m4v,video/*"
        url="http://127.0.0.1:5000/upload"
        :headers="[
          { name: 'username', value: username },
          { name: 'password', value: password }
          ]"
        style="max-width: 300px"
      />

      <div style="margin-top:15px;" class="flex flex-center">
        <q-btn color="deep-orange" @click="logout" label="Logout" />
      </div>

    </div>
  </q-page>
</template>

<script>
  export default {
    data() {
      return {
        username: localStorage.getItem("username"),
        password: localStorage.getItem("password"),
      }
    },
    methods: {
      logout() {
        localStorage.clear()
        location.reload()
      }
    }
  }
</script>
