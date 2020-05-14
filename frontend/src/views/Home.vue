<template lang="pug">
  div(class="home" align="center")
    ImageUpload
</template>

<script>
import ImageUpload from "@/components/ImageUpload.vue"
    export default {
        name: "Home",
        components:{
            ImageUpload
        }
    };
</script>
