from django.urls import path
from owner import views


urlpatterns=[
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("slots/add", views.AddTimeslotsView.as_view(), name="add-timeslots"),
    path("slots/manage", views.ManageTimeslotsView.as_view(), name="manage-timeslots"),
    path("categories/manage", views.ManageCategoriesView.as_view(), name="manage-categories"),
    path("categories/add", views.AddCategoriesView.as_view(), name="add-categories"),
    path("services/manage", views.ManageServicesView.as_view(), name="manage-services"),
    path("services/add", views.AddServicesView.as_view(), name="add-services"),
    path("services/<int:sid>", views.ServiceView.as_view(), name="view-services"),
    path("account", views.AdminAccountView.as_view(), name="account-settings"),
    path("memberships/manage", views.ManageMembershipsView.as_view(), name="manage-memberships"),
    path("memberships/add", views.AddMembershipsView.as_view(), name="add-memberships"),
    path("memberships/<int:mid>/delete", views.DeleteMembershipView.as_view(), name="delete-memberships"),
    path("beauticians/manage", views.ManageBeauticiansView.as_view(), name="manage-beauticians"),
    path("beauticians/add", views.AddBeauticiansView.as_view(), name="add-beauticians"),
    path("services/<int:sid>/delete", views.DeleteServicesView.as_view(), name="delete-services"),
    path("services/<int:sid>/update", views.UpdateServiceView.as_view(), name="update-service"),
    path("membership/<int:id>", views.detail_membership, name="view-membership"),
    path("memberships/<int:mid>/update", views.UpdateMembershipView.as_view(), name="update-membership"),
    path("categories/<int:cid>", views.DetailCategoryView.as_view(), name="view-category"),
    path("categories/<int:cid>/update", views.UpdateCategoryView.as_view(), name="update-category"),
    path("categories/<int:cid>/delete", views.DeleteCategoriesView.as_view(), name="delete-categories"),
    path("beauticians/<int:bid>", views.DetailBeauticianView.as_view(), name="view-beautician"),
    path("beautician/<int:bid>/update", views.UpdateBeauticianView.as_view(), name="update-beautician"),
    path("beauticians/<int:bid>/delete", views.DeleteBeauticianView.as_view(), name="delete-beautician"),
    path("timeslot/<int:tid>/update", views.UpdateTimeslotView.as_view(), name="update-timeslot"),
    path("timeslots/<int:tid>/delete", views.DeleteTimeslotsView.as_view(), name="delete-timeslots"),
    path("packages/manage", views.ManagePackagesView.as_view(), name="manage-packages"),
    path("giftcards/manage", views.ManageGiftCardsView.as_view(), name="manage-giftcards"),
    path("package/<int:id>", views.detail_package, name="view-package"),
    path("package/<int:pid>/delete", views.DeletePackageView.as_view(), name="delete-package"),
    path("package/<int:pid>/update", views.UpdatePackageView.as_view(), name="update-package"),
    path("packages/add", views.AddPackagesView.as_view(), name="add-packages"),
    path("giftcards/add", views.AddGiftCardsView.as_view(), name="add-giftcards"),
    path("giftcard/<int:id>", views.detail_giftcard, name="view-giftcard"),
    path("giftcards/<int:gid>/update", views.UpdateGiftCardView.as_view(), name="update-giftcard"),
    path("giftcards/<int:gid>/delete", views.DeleteGiftCardView.as_view(), name="delete-giftcard"),
    path("introoffers/manage", views.ManageIntroOffersView.as_view(), name="manage-introoffers"),
    path("introoffers/add", views.AddIntroOffersView.as_view(), name="add-introoffers"),
    path("introoffers/<int:iid>", views.DetailIntroOfferView.as_view(), name="view-introoffer"),
    path("introoffers/<int:iid>/update", views.UpdateIntroOfferView.as_view(), name="update-introoffer"),
    path("introoffers/<int:iid>/delete", views.DeleteIntroOfferView.as_view(), name="delete-introoffer"),
    path("blogs/manage", views.ManageBlogsView.as_view(), name="manage-blogs"),
    path("blogs/add", views.AddBlogsView.as_view(), name="add-blogs"),
    path("blogs/<int:bid>/update", views.UpdateBlogsView.as_view(), name="update-blog"),
    path("blogs/<int:bid>", views.DetailBlogsView.as_view(), name="view-blog"),
    path("blogs/<int:bid>/delete", views.DeleteBlogsView.as_view(), name="delete-blog"),
    path("transactions/manage", views.ManageTransactionsView.as_view(), name="manage-transactions"),
    path("transactions/add", views.AddTransactionsView.as_view(), name="add-transactions"),
    path("contactus/manage", views.ManageContactUs.as_view(), name="manage-contactus"),
    path("contactus/<int:cid>", views.DetailContactUsView.as_view(), name="view-contactus"),
    path("timeslot/<int:id>", views.detail_timeslot, name="view-timeslot"),
    path("users/manage", views.ManageUsers.as_view(), name="manage-users"),
    path("edit-password/<int:id>", views.EditPassword.as_view(), name="edit-password"),
    path("notifications", views.notifications, name="notifications"),
    path("view-notification/<int:id>", views.view_notification, name="view-notification"),
    path("careers/manage", views.ManageCareersView.as_view(), name="manage-careers"),
    path("careers/add", views.AddCareersView.as_view(), name="add-careers"),
    path("manage/bookings", views.manage_bookings, name="manage-bookings"),
    path("banner", views.ManageBanner, name="manage-banner"),
    path("banner/<int:id>/", views.UpdateBanner.as_view(), name="update-banner"),
    path("booking/calendar/", views.BookingCalendar.as_view(), name="booking-calendar"),
    path("addons/add", views.AddAddonsView.as_view(), name="add-addons"),
    path("addons", views.ManageAddonsView.as_view(), name="manage-addons"),













]