<template>
  <div class="videos">
      <section class="text-white">
          <div class="container">
          	<div class="row">
          		<div v-for="rubric in listRubrics.results" class="col">
          			<h1 class="border-danger">{{ rubric.name }}</h1>
          			<div v-for="video in rubric.videos" class="row">
          				<div class="col m-3 div">
          					<iframe width="300" height="200" class="rounded m-4"  :src="video.video" frameborder="0" allowfullscreen></iframe>
          					<p class="text-secondary mx-4">{{ video.title }}</p>
          				</div>

          			</div>
          		</div>
          	</div>
          </div>
      </section>
  </div>
</template>
<style scoped>
    /* .home {
        background: url("../assets/228.jpg");
    } */
</style>
<script>

export default {
  name: 'Videos',
  data() {
      return {
          listRubrics: []
      }
  },
  components: {},
  created() {
      this.loadlistRubrics()
  },
  methods: {
      async loadlistRubrics() {
          this.listRubrics = await fetch(
              `${this.$store.getters.getServerUrl}/videos/`
          ).then(response => response.json())
          console.log(this.listRubrics)
      }
  }
}
</script>
