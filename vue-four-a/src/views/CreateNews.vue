<template>
    <section>
        <div class="container">
        	<div class="row">
        		<div class="col-9 div m-3">
        			<h1 class="text-white border-danger">Добавить новость</h1>
        			<form class="text-white" method="post">
                        <div class="form-group row">
                            <lable class="col-md-3 col-form-label">Название</lable>
                            <div class="col-md-9">
                                <input type="text" name="title" class="form-control" placeholder="Название" required v-model="title"/>
                            </div>
                        </div>
                        <div class="form-group row">
                            <lable class="col-md-3 col-form-label">Содержание</lable>
                            <div class="col-md-9">
                                <textarea name="text" cols="40" rows="10" class="form-control" placeholder="Содержание" required v-model="text"></textarea>
                            </div>
                        </div>
                        <div class="form-group row">
                            <lable class="col-md-3 col-form-label">Ссылка на видео</lable>
                            <div class="col-md-9">
                                <input type="url" name="video" maxlength="200" class="form-control" placeholder="Ссфлка на видео" v-model="video"/>
                            </div>
                        </div>
                        <div class="form-group row">
                            <lable class="col-md-3 col-form-label">Ссылка на изображение</lable>
                            <div class="col-md-9">
                                <input type="url" name="image" maxlength="200" class="form-control" placeholder="Ссылка на изображение" required v-model="image"/>
                                <small class="form-text text-muted">Можно добавлять что-то одно из видео или изображения, если добавишь и то и то будет видно только видео.</small>
                            </div>
                        </div>
                        <div class="form-group row">
                            <lable class="col-md-3 col-form-label">Источник</lable>
                            <div class="col-md-9">
                                <input type="url" name="source" maxlength="200" class="form-control" placeholder="Источник" v-model="source"/>
                                <small class="form-text text-muted">Не обязательно</small>
                            </div>
                        </div>
                        <div class="form-group row">
                            <lable class="col-md-3 col-form-label">Автор</lable>
                            <div class="col-md-9">
                                <input type="text" name="author" maxlength="200" class="form-control" placeholder="Автор" required v-model="author"/>
                            </div>
                        </div>
        				<button class="btn btn-danger my-3" type="button" @click="sendNews()">Спасти и Сохранить</button>
        			</form>
        		</div>
        	</div>
        </div>
    </section>
</template>

<style scoped></style>

<script>
    export default {
        name: 'CreateNews',
        data() {
            return {
                title: '',
                text: '',
                video: '',
                image: '',
                source: '',
                author: '',
            }
        },
        created(){},
        methods: {
            async sendNews() {
                let data = {
                    title: this.title,
                    text: this.text,
                    video: this.video,
                    image: this.image,
                    source: this.source,
                    author: this.author
                }
                fetch(
                    `${this.$store.getters.getServerUrl}/news/create/`,
                {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                }).then(response => {
                    this.clearForm()
                    this.$router.push({name:'News'})
                })
            },
            clearForm() {
                title: this.title = ''
                text: this.text = ''
                video: this.video = ''
                image: this.image = ''
                source: this.source = ''
                author: this.author = ''

            }
        }
    }
</script>
