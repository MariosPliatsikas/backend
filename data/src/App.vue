<template>
  <div id="app">
    <form @submit.prevent="submitData">
      <label for="distance">Distance (km): </label>
      <input type="number" v-model="distance" required />
      <br />
      <label for="speed">Average Speed (km/h): </label>
      <input type="number" v-model="speed" required />
      <br />
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      distance: null,
      speed: null,
    };
  },
  methods: {
    submitData() {
      // Send data to Flask backend
      this.$axios.post('http://localhost:5000/process_data', {
        distance: this.distance,
        speed: this.speed,
      })
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error);
      });
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

