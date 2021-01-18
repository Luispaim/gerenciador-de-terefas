<template>
  <v-container fill-height>
    <v-row
      justify="center"
      align="center"
    >
      <v-col
        cols="12"
        sm="8"
        md="8"
        lg="6"
        xl="6"
      >
        <v-card class="elevation-12">
          <v-toolbar
            color="primary"
            dark
          >
            <v-toolbar-title>Dashboard</v-toolbar-title>
          </v-toolbar>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

export default {
  name: 'Dashboard',
  data: () => ({
    error: undefined

  })

}
</script>
