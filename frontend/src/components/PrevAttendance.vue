<template lang="pug">
  div.col-lg-10.ma-8
    div(v-if="dates[0]")
      v-select(:items="dates" label="Select Date" v-model="index" item-value="index" item-text="date" outlined)
    div(v-if="index!==-1")
      v-data-table.elevation-1(:headers="headers" :items="attendanceData[index]" :items-per-page="30")
</template>

<script>
    import { httpClient } from "../plugins/httpClient";
    export default {
        name: "PrevAttendance",
        data(){
            return{
                index: -1,
                dates: [],
                attendanceData: [],
                headers: [
                    { text: 'Roll no', value: 'student' },
                    { text: 'Attendance', value: 'status_display'}
                ]
            }
        },
        mounted() {
            httpClient.get('api/attendance/').then(response=>{
                let data = response.data;
                data.forEach((ele,index)=>{
                    this.dates.push({
                        date: ele.date,
                        index: index
                    });
                    this.attendanceData.push(ele.attendance);
                })
            })
        }
    }
</script>

<style scoped>

</style>
