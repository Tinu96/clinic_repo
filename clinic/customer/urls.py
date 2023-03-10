from django.urls import path
from customer import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# app_name = "customer"
urlpatterns=[
    path("login",views.LogInView.as_view(),name="login"),
    path("register", views.RegistrationView.as_view(), name="registration"),
    path("logout", views.logout_view, name="logout"),
    path("myaccount", views.MyAccountView.as_view(), name="my-account"),
    path("team",views.team,name="team"),
    path("bookingg",views.bookingg ,name="bookingg"),
    path("service",views.service,name="services"),
    path("", views.HomeView.as_view(), name="home"),
    path("book/<int:sid>", views.BookView.as_view(), name="book"),
    path("payment/<int:id>",views.booking_payment,name="booking-payment"),
    path("payment/completed>",views.payment_complete,name="payment-complete"),
    path("mybookings/all", views.MyBookingView.as_view(), name="bookings"),
    path("mybookings/<int:bid>", views.BookingUpdateView.as_view(), name="update-booking"),
    path("mybookings/<int:bid>/cancel", views.CancelBookingView.as_view(), name="cancel-booking"),
    path("shop", views.ShopView.as_view(), name="shop"),
    path("membership", views.MembershipView.as_view(), name="memberships"),
    path("booknow", views.BookingView.as_view(), name="booknow"),
    path("test", views.test, name="test"),
    path("category/<int:id>", views.category_detail, name="category-detail"),
    path("booknow/<int:cid>", views.get_category_services, name="category-services"),
    path("packages", views.PackageView.as_view(), name="packages"),
    path("giftcards", views.GiftCardView.as_view(), name="giftcards"),
    path("introoffers", views.IntroOffersView.as_view(), name="introoffers"),
    path("blogs", views.BlogsView.as_view(), name="blogs"),
    path("contactus", views.ContactUsView.as_view(), name="contactus"),
    path("aboutus", views.AboutUs.as_view(), name="aboutus"),
    path("spa-etiquette", views.SpaEti.as_view(), name="spa-etiquette"),
    path("profile-manager", views.profiledetail, name="profile-manager"),
    path("profile/<int:pid>/", views.ProfileUpdate.as_view(), name="update-profile"),
    path("wishlist/<int:sid>/", views.wishlist, name="add-wishlist"),
    path("mymemberships/<int:mid>", views.BuyMembership, name="mymem"),
    path("mymemberships/all", views.MyMembershipView.as_view(), name="my-memberships"),
    path("mypackages/<int:pid>", views.BuyPackages, name="buy-packages"),
    path("mypackages/all", views.MyPackageView.as_view(), name="my-packages"),
    path("mygiftcards/<int:gid>", views.BuyGiftCards, name="buy-giftcards"),
    path("mygiftcards/all", views.MyGiftCardsView.as_view(), name="my-giftcards"),
    path("create-profile", views.profile, name="create-profile"),
    path("membership-status/<int:id>", views.membership_status_change, name="membership-status"),
    path("package-status/<int:id>", views.package_status_change, name="package-status"),
    path("giftcard-status/<int:id>", views.giftcard_status_change, name="giftcard-status"),
    path("service-review/<int:id>", views.service_review, name="service-review"),
    path("change-password", views.change_password, name="change-password"),
    path("booking-status/<int:id>", views.booking_status_change, name="booking-status-change"),
    path("wishlist", views.WishlistView.as_view(), name="wishlist"),
    path("wishlist-delete/<int:id>", views.delete_wishlist, name="wishlist-delete"),
    path("cart-giftcard/<int:id>", views.cart_giftcard, name="cart-giftcard"),
    path("cart-items", views.cart_items, name="cart-items"),
    path("service-cart", views.service_cart, name="service-cart"),
    path("service-cart/remove/<int:id>", views.remove_service_cart, name="remove-service-cart"),
    path("cart/payment", views.payment_cart_complete, name="cart-payment"),
    path("cart-delete/<int:id>", views.delete_cart_item, name="cart-delete"),
    path("cart-membership/<int:id>", views.cart_membership, name="cart-membership"),
    path("myintrooffers/<int:id>", views.BuyIntroOffers, name="buy-introoffers"),
    path("cart-introoffer/<int:id>", views.cart_introoffer, name="cart-introoffer"),
    path("cart-package/<int:id>", views.cart_package, name="cart-package"),
    path("first_visit", views.first_visit, name="first-visit"),
    path("mani-pedi", views.mani_pedi, name="mani-pedi"),
    path("manicure", views.manicure, name="manicure"),
    path("pedicure", views.pedicure, name="pedicure"),
    path("hair-removal", views.hair_removal, name="hair-removal"),
    path("add-ons", views.add_ons, name="add-ons"),
    path("massage", views.massage, name="massage"),
    path("eye", views.eye, name="eye"),
    path("facials", views.facials, name="facials"),
    path("payment", views.payment, name="payment"),
    path("membership-payment/<int:id>", views.membership_payment, name="membership-payment"),
    path("package-payment/<int:id>", views.package_payment, name="package-payment"),
    path("giftcard-payment/<int:id>", views.giftcard_payment, name="giftcard-payment"),
    path("subscription", views.subscription, name="subscription"),
    path("book-details/<int:id>", views.book_details, name="book-details"),
    path("book-review/<int:id>", views.book_review, name="book-review"),
    path("service-orders", views.my_orders, name="service-orders"),
    # Password reset paths
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_complete.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path("careers", views.careers, name="careers"),
    path("career-form", views.CareerForm.as_view(), name="career-form"),
    path("ajax", views.test_ajax, name="ajax"),

    # path("mygiftcards/all", views.MyGiftCardView.as_view(), name="my-giftcards"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)