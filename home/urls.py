from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect, HttpResponse
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
urlpatterns = [
    path('', views.home, name="home"),
    path('features', views.features, name="features"),
    path('use_cases_strategy', views.use_cases_strategy, name="use_cases_strategy"),
    path('use_cases_invester', views.use_cases_invester, name="use_cases_invester"),
    path('Open_interest_analysis', views.Open_interest_analysis,
         name='Open_interest_analysis'),
    path('Strategy_builder_straddle', views.Strategy_builder_straddle,
         name='Strategy_builder_straddle'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('help_support', views.help_support, name='help_support'),
    path('learning_center', views.learning_center, name='learning_center'),
    path('blog', views.blog, name='blog'),
    path('reset_password', views.reset_password, name='reset_password'),
    path('signUp', views.signUp, name='signUp'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('change_pass/<token>/', views.change_pass, name='change_pass'),
    path('get_option_chain/', views.get_option_chain, name='get_option_chain'),
    path('Algo_market_place', views.Algo_market_place, name='Algo_market_place'),
    path('my_strategies', views.my_strategies, name='my_strategies'),
    path('my_portfolio', views.my_portfolio, name='my_portfolio'),
    path('broking_details', views.broking_details, name='broking_details'),
    path('chart_topgainer', views.chart_topgainer, name='chart_topgainer'),
    path('Futures_Buildup', views.Futures_Buildup, name='Futures_Buildup'),
    path('contact_us', views.contact_us, name='contact_us'),
#     path('base', views.base, name='base'),
    path('option_strategies', views.option_strategies, name='option_strategies'),
    path('strategy_builder', views.strategy_builder, name='strategy_builder'),
    path('market_glance', views.market_glance, name='market_glance'),
    path('financial_result', views.financial_result, name='financial_result'),
    path('reports', views.reports, name='reports'),
    path('stock_scanner', views.stock_scanner, name='stock_scanner'),
    path('rocket_call', views.rocket_call, name='rocket_call'),
    path('holiday', views.holiday, name='holiday'),
    path('lot_size', views.lot_size, name='lot_size'),
    path('market_heavy', views.market_heavy, name='market_heavy'),
    path('bulk_deal_data', views.bulk_deal_data, name='bulk_deal_data'),
    path('bulk_deal_data_page', views.bulk_deal_data_page,
         name='bulk_deal_data_page'),
    path('dashboard1', views.dashboard1, name='dashboard1'),
    path('base_dashboard1', views.base_dashboard1, name='base_dashboard1'),
    path('global_market', views.global_market, name='global_market'),
    path('market_actions', views.market_actions, name='market_actions'),
    path('ban_list_dashboard', views.ban_list_dashboard, name='ban_list_dashboard'),
    # path('stock-listing/', views.stock_listing, name='stock_listing'),
    path('delete_user/<str:id>', views.delete_user, name='delete_user'),
    path('manage_user', views.manage_user, name='manage_user'),
    path('admin_reset', views.admin_reset, name='admin_reset'),
    path('admin_signup', views.admin_signup, name='admin_signup'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('courses_details', views.courses_details, name='courses_details'),
    path('market_wide_position', views.market_wide_position,
         name='market_wide_position'),
    path('dii_fii', views.dii_fii, name='dii_fii'),
    path('stock_analysis', views.stock_analysis, name='stock_analysis'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),

    path('put_call_ratio_chart', views.put_call_ratio_chart,
         name='put_call_ratio_chart'),

    path('filtered_oi_data', views.filtered_oi_data, name='filtered_oi_data'),
    path('filtered_oi_change_data', views.filtered_oi_change_data,
         name='filtered_oi_change_data'),
    path('scale_stacking_chart', views.scale_stacking_chart,
         name='scale_stacking_chart'),
    path('pcr_volume', views.pcr_volume, name='pcr_volume'),

    path('Edit_user_data/<str:id>', views.Edit_user_data, name='Edit_user_data'),

    path('volume-shocker/', views.volume_shocker, name='volume_shocker'),
    path('admin_panel', views.admin_panel, name='admin_panel'),
    path('put_call_ratio', views.put_call_ratio, name='put_call_ratio'),
    path('feedback_management', views.feedback_management,
         name='feedback_management'),
    path('payments_details', views.payments_details, name='payments_details'),


    path('oi_gainers', views.oi_gainers, name='oi_gainers'),
    path('oi_losers', views.oi_losers, name='oi_losers'),
    path('dii_fii', views.dii_fii, name='dii_fii'),

    path('performance_data', views.performance_chart, name='performance_chart'),
    path('nifty_tracker', views.nifty_tracker, name='nifty_tracker'),
    path('get_52_week_data', views.get_52_week_data, name='get_52_week_data'),
    path('get_52_week_low_data', views.get_52_week_low_data,
         name='get_52_week_low_data'),
    path('only_buyers', views.only_buyers, name='only_buyers'),
    path('get_data_buildup/', views.get_data_buildup, name='get_data_buildup'),
    path('watch_list', views.watch_list, name='watch_list'),
    path('port_folio_management', views.port_folio_management,
         name='port_folio_management'),
    path('options_simulator', views.options_simulator, name='options_simulator'),
    path('new_options_data', views.new_options_data, name='new_options_data'),
    path('admin_report', views.admin_report, name='admin_report'),
    path('feedback', views.feedback, name='feedback'),
    path('stock_list', views.stock_list, name='stock_list'),
    path('blog_news', views.blog_news, name='blog_news'),
    path('blog_news_data', views.blog_news_data, name='blog_news_data'),
    path('contributor', views.contributor, name='contributor'),
    path('contributors_data', views.contributors_data, name='contributors_data'),
    path('future_data_chart', views.future_data_chart, name='future_data_chart'),
    path('stock_future', views.stock_future, name='stock_future'),
#     path('contrib_test', views.contrib_test, name='contrib_test'),
    path('get-news-data/', views.get_news_data, name='get_news_data'),
    path('get-news-data/', views.get_news_data, name='get_news_data'),
    path('stock_option_chain', views.stock_option_chain, name='stock_option_chain'),
    path('option_dashboard', views.option_dashboard, name='option_dashboard'),



    path('fetch_option_data_with_spot_price', views.fetch_option_data_with_spot_price, name='fetch_option_data_with_spot_price'),
    path('breakout_data', views.breakout_data, name='breakout_data'),
    path('volume_socker', views.volume_socker, name='volume_socker'),
    path('get_gainers_data_separate', views.get_gainers_data_separate, name='get_gainers_data_separate'),
    path('top_gainers', views.top_gainers, name='top_gainers'),
    path('get_loosers_data_separate', views.get_loosers_data_separate, name='get_loosers_data_separate'),
    path('top_loosers', views.top_loosers, name='top_loosers'),
    path('get_gap_data', views.get_gap_data, name='get_gap_data'),
    path('gap_up_gap_down', views.gap_up_gap_down, name='gap_up_gap_down'),
    path('save_to_watchlist', views.save_to_watchlist, name='save_to_watchlist'),
    path('get_watchlist_data', views.get_watchlist_data, name='get_watchlist_data'),
    path('delete_watchlist_item/<str:item_id>', views.delete_watchlist_item, name='delete_watchlist_item'),

    path('get_intraday_breakout_data', views.get_intraday_breakout_data, name='get_intraday_breakout_data'),
    path('intraday_breakouts', views.intraday_breakouts, name='intraday_breakouts'),


    path('opening_clue_data_view', views.opening_clue_data_view, name='opening_clue_data_view'),
    path('opening_price_clues', views.opening_price_clues, name='opening_price_clues'),
    path('base_api_border_top', views.base_api_border_top, name='base_api_border_top'),
    path('get_derivative_data', views.get_derivative_data, name='get_derivative_data'),
    path('derivative_summary', views.derivative_summary, name='derivative_summary'),
    path('future_dashboard_charts', views.future_dashboard_charts, name='future_dashboard_charts'),
    path('nse_volume_shocker', views.nse_volume_shocker, name='nse_volume_shocker'),
    path('nse_most_active_stock', views.nse_most_active_stock, name='nse_most_active_stock'),
    path('nse_most_spread_stock', views.nse_most_spread_stock, name='nse_most_spread_stock'),
    path('dashboard_news_feed', views.dashboard_news_feed, name='dashboard_news_feed'),
#     path('strangle_chart', views.strangle_chart, name='strangle_chart'),
#     path('get_straddle_backtest_data', views.get_straddle_backtest_data, name='get_straddle_backtest_data'),
#     path('straddle_payoff', views.straddle_payoff, name='straddle_payoff'),
#     path('fetch_expiry_data_option_strategies', views.fetch_expiry_data_option_strategies, name='fetch_expiry_data_option_strategies'),
    path('get_expiry_data/<str:symbol>/', views.get_expiry_data, name='get_expiry_data'),
    path('option_simulator_data', views.option_simulator_data, name='option_simulator_data'),
    path('straddle_data', views.straddle_data, name='straddle_data'),
    path('option_strategies/long_call_option', views.long_call_option, name='long_call_option'),
    path('option_strategies/long_put_option', views.long_put_option, name='long_put_option'),
    path('option_strategies/covered_call', views.covered_call, name='covered_call'),
    path('option_strategies/short_call_option', views.short_call_option, name='short_call_option'),
    path('option_strategies/synthetic_long_call', views.synthetic_long_call, name='synthetic_long_call'),
    path('option_strategies/covered_put', views.covered_put, name='covered_put'),
    path('option_strategies/long_combo', views.long_combo, name='long_combo'),
    path('option_strategies/long_straddle', views.long_straddle, name='long_straddle'),
    path('option_strategies/short_straddle', views.short_straddle, name='short_straddle'),
    path('option_strategies/pretective_call', views.pretective_call, name='pretective_call'),
    path('aaaa', views.aaaa, name='aaaa'),





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)




# Import your app's views here
# For example, if your app is named 'myapp':
# from myapp import views



# Custom 404 page
def custom_404_view(request, exception=None):
    return render(request, '404/404.html', status=404)

handler404 = custom_404_view
