<template>
  <q-page class="flex flex-center">
    <div>

      <div>
        <q-input style="margin-bottom:15px;" v-model="username" placeholder="Enter username" filled type="text" />
      </div>

      <div>
        <q-input v-model="password" filled type="password" placeholder="Enter password" />
      </div>

      <div  style="margin-top:15px;" class="flex flex-center">
        <q-btn color="primary" label="Login" @click="sendCred" />
      </div>

    </div>
  </q-page>
</template>


<script>
export default {
  data() {
    return {
      username: "", password: ""
    }
  },
  methods: {
    async sendCred() {
      localStorage.setItem("username", this.username)
      localStorage.setItem("password", this.password)
      location.reload()
      // const res = await fetch("http://127.0.0.1:8000/login", {
      //   method: "POST",
      //   headers: {
      //     'Content-Type': 'application/json',
      //   },
      //   body: JSON.stringify({ username: this.username, password: this.password}),
      // })
      // const data = await res.json()
      // console.log(data)
    }
  }
}
</script>
