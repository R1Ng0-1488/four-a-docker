<template>
    <div class="row">
        <div class="col-xs-12 col-lg-8 m-3 div">
            <h3 class="text-white">Добавить комментарий</h3>
            <form class="" method="post">
                <div class="form-group row">
                    <label class="col-md-3 col-form-label">Автор</label>
                    <div class="col-md-9">
                        <input class="form-control" type="text" name="author" placeholder="Автор" required v-model="author"/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-md-3 col-form-label">Содержание</label>
                    <div class="col-md-9">
                        <textarea class="form-control" type="text" name="content" cols="40" rows="10" placeholder="Содержание" required
                        v-model="content"/></textarea>
                    </div>
                </div>
                <button class="btn btn-danger m-3" type="button" name="button" @click="sendComment()">Добавить</button>
            </form>
        </div>
    </div>
</template>

<style scoped>

</style>

<script>
 export default {
     name: "Comment",
     props: ["news", "images", "texts"],
     data() {
         return {
             author: '',
             content: '',
             news: '',
             images: '',
             texts: ''
         }
     },
     created() {},
     methods: {
         async sendComment() {
             let data = {
                 author: this.author,
                 content: this.content,
                 news: this.news,
                 images: this.images,
                 texts: this.texts
             }
             fetch(
                 `${this.$store.getters.getServerUrl}/comments/create/`,
                 {
                     method: 'POST',
                     headers: {
                         'Content-Type': 'application/json'
                     },
                     body: JSON.stringify(data)
                 }).then(response => {
                     this.$emit('reLoad')
                     this.clearForm()
                 })
         },
         clearForm() {
             author: this.author = ''
             content: this.content = ''
             news: this.news = null
             images: this.images = null
             texts: this.texts = null
         }
     }
 }
</script>
