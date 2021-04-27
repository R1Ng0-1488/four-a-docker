<template>
<section>
    <div class="container">
        <div class="row">
            <div class="col div m-3">
                <h1 class="text-white"> {{ texts.title }} </h1>
                <p class="text-white"> {{texts.text}} </p>
                <p class="text-white"> {{texts.published}} </p>
            </div>
        </div>
        <!-- comment form  -->
        <Comment :texts="texts.id" @reLoad="loadTexts()"/>
        <div v-for="comment in texts.comments_texts" class="row">
            <div class="col-12 div m-3">
                <h3 class="text-white"> {{comment.author}} </h3>
                <p class="text-white"> {{comment.content}} </p>
                <p class="text-white"> {{comment.published}} </p>
            </div>
        </div>
    </div>
</section>
</template>

<style scoped>

</style>

<script>
import Comment from "../components/Comment"
export default {
    name: 'SingleTexts',
    props: ['id'],
    components: {Comment},
    data() {
        return {
            texts: {}
        }
    },
    created() {
        this.loadTexts()
    },
    methods: {
        async loadTexts() {
            this.texts = await fetch(
                `${this.$store.getters.getServerUrl}/texts/${this.id}/`
            ).then(response => response.json())
            console.log(this.texts)
        }
    }
}
</script>
