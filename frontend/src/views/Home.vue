<template lang="pug">
  div(class="home" align="center")
    img(alt="" src="../assets/download.png")
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
