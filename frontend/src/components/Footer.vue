<template lang="pug">
  v-footer(color="blue" padless)
    v-row(justify="center" no-gutters)
      v-btn.py-2(v-for="link in links" :key="link" color="white" icon)
        v-icon {{link}}
    v-col.py-4.text-center.white--text.font-weight-bold(color="secondary" cols="12") {{ new Date().getFullYear() }} — Face Attendance
</template>

<script>
    export default {
        data() {
            return {
                links: ["mdi-gmail", "mdi-facebook", "mdi-instagram", "mdi-github"]
            };
        }
    };
</script>
