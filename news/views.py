from django.shortcuts import render, get_list_or_404, HttpResponse
from django.views.generic import ListView
from .models import News, Category
from .forms import ContactForm
from django.core.paginator import Paginator


def home(request):
    news = News.published.all().order_by('-published_time')[:4]
    categories = Category.objects.all()
    s_category = News.objects.filter(category__name="Sport").order_by("-published_time")[:4]
    i_category = News.objects.filter(category__name="Ilmiy").order_by("-published_time")[:4]
    m_category = News.objects.filter(category__name="Madaniy-ma'rifiy").order_by("-published_time")[:4]
    d_category = News.objects.filter(category__name="Dunyo").order_by("-published_time")[:4]
    context = {
        "news": news,
        "category": categories,
        "s_category": s_category,
        "i_category": i_category,
        "d_category": d_category,
        "m_category": m_category,
    }
    return render(request, 'news/home.html', context)


# class HomePageView(ListView):
#     model = News
#     template_name = 'news/home.html'
#     context_object_name = 'news'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = self.model.objects.all()
#         context['s_category'] = News.published.filter(category__name="Sport").order_by("-published_time")[:4]
#         context['i_category'] = News.published.filter(category__name="Ilmiy").order_by("-published_time")[:4]
#         context['m_category'] = News.published.filter(category__name="Madaniy-ma'rifiy").order_by("-published_time")[:4]
#         context['d_category'] = News.published.filter(category__name="Dunyo").order_by("-published_time")[:4]
#
#         return context


def news_list(request):
    post_list = News.published.all()
    context = {
        "news_list": post_list,
    }
    return render(request, "news/list.html", context)


def blog(request):
    blog_list = News.objects.all()  #.order_by("-published_time")[:4]
    # categorys = Category.objects.all()
    paginator = Paginator(blog_list, 2)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    # if not page:
    #     page = 1
    # print(page_num)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        "count": blog_list.count(),
        # "blog_list": paginator,
        "blog_list": page,
        # "categorys": categorys,
        # "page_object": page,
        # "page": paginator
    }
    return render(request, "news/blog.html", context)


def detail(request, news):
    # news = News.objects.get(id=pk)
    news = get_list_or_404(News, slug=news, status=News.Status.Published)[:4]
    categories = Category.objects.all()
    context = {
        "news": news,
        "category": categories
    }
    return render(request, "news/single-blog.html", context)


def category(request):
    news = News.published.all().order_by('-published_time')[:4]
    categorys = Category.objects.all()
    context = {
        "news": news,
        "category": categorys,
    }
    return render(request, 'news/categori.html', context)

# def sport(request):
#     s_news = News.published().order_by('-published_time')
#     s_category = Category.objects.all().filter(category__name="Sport")
#     context = {
#         "s_news": s_news,
#         "s_category": s_category,
#     }
#
#     return render(request, 'news/sport.html', context)


class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Sport")
        return news


class SinceNewsView(ListView):
    model = News
    template_name = 'news/ilmiy.html'
    context_object_name = 'ilmiy_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Ilmiy")
        return news


class CulturalNewsView(ListView):
    model = News
    template_name = 'news/madaniy.html'
    context_object_name = 'madaniy_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Madaniy-ma'rifiy")
        return news


class ForeignNewsView(ListView):
    model = News
    template_name = 'news/xorij.html'
    context_object_name = 'xorij_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Dunyo")
        return news


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h3> Xabaringiz uchun tashakkur! </h3>")
    context = {
        "form": form,
    }

    return render(request, 'news/contact.html', context)


def about(request):

    return render(request, 'news/about.html', )



