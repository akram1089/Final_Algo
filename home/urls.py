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
    path('option_strategy_optimizer', views.option_strategy_optimizer, name='option_strategy_optimizer'),
    path('get_stock_symbol', views.get_stock_symbol, name='get_stock_symbol'),
    path('get_option_strategy_optimizer_spot_data', views.get_option_strategy_optimizer_spot_data, name='get_option_strategy_optimizer_spot_data'),
    path('get_option_strategy_optimizer_option_data', views.get_option_strategy_optimizer_option_data, name='get_option_strategy_optimizer_option_data'),
    path('option_strategies_expiry', views.option_strategies_expiry, name='option_strategies_expiry'),
    path('get_payoff_data/', views.get_payoff_data, name='get_payoff_data'),
    path('filter_iv_data', views.filter_iv_data, name='filter_iv_data'),
    path('bse_spot_data', views.bse_spot_data, name='bse_spot_data'),
    path('option_strategy_tester', views.option_strategy_tester, name='option_strategy_tester'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('customer_contact', views.customer_contact, name='customer_contact'),
    path('vertical', views.vertical, name='vertical'),
    path('annotation', views.annotation, name='annotation'),
    path('bse_option_chain',views.bse_option_chain, name = 'bse_option_chain' ),
    path('bse_option_chain_spotprice',views.bse_option_chain_spotprice, name = 'bse_option_chain_spotprice' ),
    path('bse_option_expiry',views.bse_option_expiry, name = 'bse_option_expiry' ),
    path('bse_table_data',views.bse_table_data, name = 'bse_table_data'),
    path('customer_feedback_data', views.customer_feedback_data,name='customer_feedback_data'),
    path('customer_feedback', views.customer_feedback,name='customer_feedback'),
    path('format_feedback_data', views.format_feedback_data,name='format_feedback_data'),
    path('event_tracker_dates', views.event_tracker_dates,name='event_tracker_dates'),
    path('event_tracker', views.event_tracker,name='event_tracker'),
    path('subscribe_to_newsletter', views.subscribe_to_newsletter, name ='subscribe_to_newsletter'),
    path('get_subscribers/', views.get_subscribers, name='get_subscribers'),
    path('subscribers_management', views.subscribers_management, name='subscribers_management'),
    path('event_tracker', views.event_tracker, name ='event_tracker'),
    path('event_tracker_dates', views.event_tracker_dates, name ='event_tracker_dates'),
    path('events_table_data', views.events_table_data, name ='events_table_data'),
    path('broker_management', views.broker_management, name ='broker_management'),
    path('save_zerodha_config', views.save_zerodha_config, name='save_zerodha_config'),
    path('get_zerodha_config', views.get_zerodha_config, name='get_zerodha_config'),
    path('delete_zerodha_config/<int:item_id>/', views.delete_zerodha_config, name='delete_zerodha_config'),
    path('edit_access_token', views.edit_access_token, name='edit_access_token'),
    path('zerodha_place', views.zerodha_place, name='zerodha_place'),
    path('kiteOrder', views.kiteOrder, name='kiteOrder'),
    path('ipo_dashboard', views.ipo_dashboard, name='ipo_dashboard'),
    path('ipo_return_data', views.ipo_return_data, name='ipo_return_data'),
    path('best_performers', views.best_performers, name='best_performers'),
    path('draft_prospectus', views.draft_prospectus, name='draft_prospectus'),
    path('quote_data_zerodha', views.quote_data_zerodha, name='quote_data_zerodha'),
    path('mutual_fund', views.mutual_fund, name='mutual_fund'),
    path('category_performance', views.category_performance, name='category_performance'),
    path('check_user_logged_in', views.check_user_logged_in, name='check_user_logged_in'),
    
    path('ipo_watch', views.ipo_watch, name='ipo_watch'),
    path('new_listed_ipo', views.new_listed_ipo, name='new_listed_ipo'),
    path('basic_allotment', views.basic_allotment, name='basic_allotment'),
    path('ipo_news', views.ipo_news, name='ipo_news'),
    path('ipo_deepak', views.ipo_deepak, name='ipo_deepak'),
    path('news_details/<int:sno>/<str:heading>/', views.news_details, name='news_details'),
    path('option_index_statregy_executor', views.option_index_statregy_executor, name='option_index_statregy_executor'),

    path('mutual_funds', views.mutual_funds, name ='mutual_funds'),
    path('category_performance', views.category_performance, name='category_performance'),
    path('holdings_select', views.holdings_select, name='holdings_select'),
    path('performances_data', views.performances_data, name='performances_data'),
    path('fund_activity', views.fund_activity, name='fund_activity'),
    path('whats_in_out_category', views.whats_in_out_category, name='whats_in_out_category'),
    path('whats_table_val', views.whats_table_val, name='whats_table_val'),
    path('dividend_data', views.dividend_data, name='dividend_data'),
    path('dividend_category', views.dividend_category, name='dividend_category'),
    path('dividend_date', views.dividend_date, name='dividend_date'),
    path('dividend_datas', views.dividend_datas, name='dividend_datas'),
    path('fund_profile', views.fund_profile, name='fund_profile'),
    path('new_funds_offer', views.new_funds_offer, name='new_funds_offer'),
    path('mutual_fund_news', views.mutual_fund_news, name='mutual_fund_news'),
    path('mutual_news_details', views.mutual_news_details, name='mutual_news_details'),
    path('top_holdings_fund_house', views.top_holdings_fund_house, name='top_holdings_fund_house'),
    path('top_holdings_category', views.top_holdings_category, name='top_holdings_category'),
    path('holdings_scheme', views.holdings_scheme, name='holdings_scheme'),
    path('mutual_fund_performance', views.mutual_fund_performance, name='mutual_fund_performance'),

    path('main_holding_table_data', views.main_holding_table_data, name='main_holding_table_data'),
    
    path('main_nav_data', views.main_nav_data, name='main_nav_data'),
    path('main_nav_historical_data', views.main_nav_historical_data, name='main_nav_historical_data'),
    path('All_nav_historical_table_data', views.All_nav_historical_table_data, name='All_nav_historical_table_data'),
    path('All_ipo_news', views.All_ipo_news, name='All_ipo_news'),
    path('All_mutual_news', views.All_mutual_news, name='All_mutual_news'),
    path('icon_algo_trade', views.icon_algo_trade, name='icon_algo_trade'),
    path('short_put', views.short_put, name='short_put'),
    path('bull_call_spread', views.bull_call_spread, name='bull_call_spread'),
    path('bull_put_spread', views.bull_put_spread, name='bull_put_spread'),
    path('call_ratio_back_spread', views.call_ratio_back_spread, name='call_ratio_back_spread'),
    path('long_synthetic', views.long_synthetic, name='long_synthetic'),
    path('range_forward', views.range_forward, name='range_forward'),
    path('bullish_butterfly', views.bullish_butterfly, name='bullish_butterfly'),
    path('bullish_condor', views.bullish_condor, name='bullish_condor'),
    path('bear_call_spread', views.bear_call_spread, name='bear_call_spread'),
    path('bear_put_spread', views.bear_put_spread, name='bear_put_spread'),
    path('put_ratio_back_spread', views.put_ratio_back_spread, name='put_ratio_back_spread'),
    path('short_synthetic', views.short_synthetic, name='short_synthetic'),
    path('risk_reversal', views.risk_reversal, name='risk_reversal'),
    path('bearish_butterfly', views.bearish_butterfly, name='bearish_butterfly'),
    path('bearish_condor', views.bearish_condor, name='bearish_condor'),
    path('long_strangle', views.long_strangle, name='long_strangle'),
    path('short_strangle', views.short_strangle, name='short_strangle'),
    path('jade_lizard', views.jade_lizard, name='jade_lizard'),
    path('reverse_jade_lizard', views.reverse_jade_lizard, name='reverse_jade_lizard'),
    path('call_ratio_spread', views.call_ratio_spread, name='call_ratio_spread'),
    path('put_ratio_spread', views.put_ratio_spread, name='put_ratio_spread'),
    path('batman_startegy', views.batman_startegy, name='batman_startegy'),
    path('long_iron_fly', views.long_iron_fly, name='long_iron_fly'),
    path('short_iron_fly', views.short_iron_fly, name='short_iron_fly'),
    path('double_fly', views.double_fly, name='double_fly'),
    path('long_iron_condor', views.long_iron_condor, name='long_iron_condor'),
    path('short_iron_condor', views.short_iron_condor, name='short_iron_condor'),
    path('double_condor', views.double_condor, name='double_condor'),
    path('offer_for_sale', views.offer_for_sale, name='offer_for_sale'),
    path('test', views.test, name='test'),
    path('content_management', views.content_management, name='content_management'),

    path('save_note', views.save_note, name='save_note'),
    path('get_notes', views.get_notes, name='get_notes'),
    path('save_strategy', views.save_strategy, name='save_strategy'),
    path('get_all_strategies', views.get_all_strategies, name='get_all_strategies'),
    path('delete_strategy', views.delete_strategy, name='delete_strategy'),
    path('get_unique_strategy', views.get_unique_strategy, name='get_unique_strategy'),
    path('update_strategy', views.update_strategy, name='update_strategy'),


    path('fetch_indices_data', views.fetch_indices_data, name='fetch_indices_data'),
    path('account_details', views.account_details, name='account_details'),
    path('broker_details', views.broker_details, name='broker_details'),
    path('zerodha_api_config', views.zerodha_api_config, name='zerodha_api_config'),

    path('main_contributor/<str:contributor>/', views.main_contributor, name='main_contributor'),


    path('api_managements', views.api_managements, name='api_managements'),
    path('save_broker_admin', views.save_broker_admin, name='save_broker_admin'),
    path('get_api_integrations_admin', views.get_api_integrations_admin, name='get_api_integrations_admin'),
    path('save_broker_name', views.save_broker_name, name='save_broker_name'),
    path('get_all_broker_names', views.get_all_broker_names, name='get_all_broker_names'),
    path('edit_broker_admin_data', views.edit_broker_admin_data, name='edit_broker_admin_data'),
    path('delete_record', views.delete_record, name='delete_record'),
    path('add_edit_access_token', views.add_edit_access_token, name='add_edit_access_token'),
    path('edit_api_details_admin', views.edit_api_details_admin, name='edit_api_details_admin'),
    path('update_api_credentials_admin', views.update_api_credentials_admin, name='update_api_credentials_admin'),
    path('margin_calculations', views.margin_calculations, name='margin_calculations'),

    path('stock_option_chart', views.stock_option_chart, name='stock_option_chart'),
    path('get_all_stocks', views.get_all_stocks, name='get_all_stocks'),
    path('get_spot_data', views.get_spot_data, name='get_spot_data'),
    path('get_expiry_date', views.get_expiry_date, name='get_expiry_date'),
    path('india_vix_stock', views.india_vix_stock, name='india_vix_stock'),
    path('open_interest', views.open_interest, name='open_interest'),
    path('change_oi_val', views.change_oi_val, name='change_oi_val'),
    path('put_call_data', views.put_call_data, name='put_call_data'),

    
    path('angel_one_margin_calculations', views.angel_one_margin_calculations, name='angel_one_margin_calculations'),
    




  




    # other URL configurations




    



    





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
