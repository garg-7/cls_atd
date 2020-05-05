<template lang="pug">
  div(class="home" align="center")
    h2.ma-12 Upload the Image of Classroom to get Attendance
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
