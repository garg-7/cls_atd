<template lang="pug">
  div(class="home" align="center")
    div(v-if="step===0")
      h1.ma-12 Welcome to Face Attendance App :)
      v-btn.ma-12.white--text( @click = "step=1" color="blue") Previous Attendance
      v-btn.ma-12.white--text(@click = "step=2" color="blue") New Attendance
    div(v-if="step===1")
      PrevAttendance
    div(v-if="step===2")
      ImageUpload
</template>

<script>
import ImageUpload from "@/components/ImageUpload.vue"
import PrevAttendance from "../components/PrevAttendance";
    export default {
        name: "Home",
        components:{
            ImageUpload,
            PrevAttendance
        },
        data() {
            return{
              step: 0
          }
        }
    };
</script>
