<template>
    <v-chip :color="getColor(value)"> {{ value }} </v-chip>
</template>

<script>
export default {
    props: ["value"],
    methods: {
        getColor (logged) {
            return logged > 0 ? 'green' : 'gray'
        }
    }
}
</script>

<style>

</style>