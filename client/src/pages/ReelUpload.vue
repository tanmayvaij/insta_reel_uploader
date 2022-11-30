<template>
  <q-page class="flex flex-center">
    <div>

      <div>
        <q-file color="teal" outlined v-model="model" label="Label">
          <template v-slot:append>
            <q-avatar>
              <img src="https://cdn.quasar.dev/logo-v2/svg/logo.svg" />
            </q-avatar>
          </template>
        </q-file>
      </div>

      <div style="margin-top: 15px" class="flex flex-center">
        <q-btn color="primary" label="Upload" />
      </div>
      
    </div>
  </q-page>
</template>

<script></script>
