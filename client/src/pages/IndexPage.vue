<template>
  <q-page class="flex flex-center">
    <div>

      <div>
        <q-input style="margin-bottom:15px;" v-model="username" placeholder="Enter username" filled type="text" />
      </div>

      <div>
        <q-input v-model="password" placeholder="Enter password" filled :type="isPwd ? 'password' : 'text'">
          <template v-slot:append>
            <q-icon :name="isPwd ? 'visibility_off' : 'visibility'" class="cursor-pointer" @click="isPwd = !isPwd" />
          </template>
        </q-input>
      </div>

    </div>
  </q-page>
</template>


<script>
import { ref } from 'vue'

export default {
  setup () {
    return {
      username: ref(''),
      isPwd: ref(true)
    }
  }
}
</script>